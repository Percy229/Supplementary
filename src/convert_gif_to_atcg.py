import argparse
from PIL import Image, ImageSequence
import os
import random
import pandas as pd
import numpy as np

color_to_base = {
    (255, 0, 0): 'A',
    (0, 0, 255): 'C',
    (255, 255, 0): 'G',
}

def map_to_closest_color_and_base(color):
    red, green, blue = color
    if red > 127 and green < 127 and blue < 127:
        return 'A'
    elif red < 127 and green < 127 and blue > 127:
        return 'C'
    elif red > 127 and green > 127 and blue < 127:
        return 'G'
    else:
        return 'T'

def generate_random_dna(length):
    return ''.join(random.choice('ACGT') for _ in range(length))

def process_gif(gif_path, output_dir):
    gif_name = os.path.splitext(os.path.basename(gif_path))[0]
    output_file = os.path.join(output_dir, f"{gif_name}_dna_sequences.txt")

    try:
        gif = Image.open(gif_path)
    except IOError:
        print("Unable to open GIF file, please check the file path and whether the file exists.")
        return None, None, None

    position_dna_sequences = {}

    for frame_index, frame in enumerate(ImageSequence.Iterator(gif), start=1):
        frame_rgb = frame.convert('RGB')
        width, height = frame_rgb.size

        for y in range(height):
            for x in range(width):
                pixel_color = frame_rgb.getpixel((x, y))
                base = map_to_closest_color_and_base(pixel_color)
                if (x, y) not in position_dna_sequences:
                    position_dna_sequences[(x, y)] = []
                position_dna_sequences[(x, y)].append(base)

    with open(output_file, 'w') as f:
        for (x, y), bases in sorted(position_dna_sequences.items()):
            dna_sequence = ''.join(bases)
            f.write(f"At position ({x}, {y}): {dna_sequence}\n")

    random_dna_sequences = []
    for _ in range(3):
        unique_random_dna = set()
        while len(unique_random_dna) < 1000:
            unique_random_dna.add(generate_random_dna(120))
        random_dna_sequences.append(list(unique_random_dna))

    match_counts = []
    for i in range(3):
        matching_count = 0
        matched_random_sequences = set()
        for random_dna in random_dna_sequences[i]:
            if random_dna in matched_random_sequences:
                continue
            for dna_sequence in position_dna_sequences.values():
                gif_dna = ''.join(dna_sequence)
                if gif_dna in random_dna:
                    matching_count += 1
                    matched_random_sequences.add(random_dna)
                    break
        match_counts.append(matching_count)

    average_matching_count = np.mean(match_counts)
    std_dev_matching_count = np.std(match_counts)

    return match_counts, average_matching_count, std_dev_matching_count

def main():
    parser = argparse.ArgumentParser(description='Process GIF files to extract DNA sequences and perform comparisons.')
    parser.add_argument('folder_path', type=str, help='Path to the folder containing GIF files')
    parser.add_argument('output_path', type=str, help='Path to save the output CSV file')
    args = parser.parse_args()

    folder_path = args.folder_path
    output_file = args.output_path

    gif_files = [f for f in os.listdir(folder_path) if f.endswith('.gif')]
    results = []

    for gif_file in gif_files:
        gif_path = os.path.join(folder_path, gif_file)
        match_counts, avg_match_count, std_dev_match_count = process_gif(gif_path, folder_path)
        if match_counts is not None:
            results.append({'GIF_File': gif_file,
                            'Match_Counts1': match_counts[0], 'Match_Counts2': match_counts[1], 'Match_Counts3': match_counts[2],
                            'Avg_Match_Counts': avg_match_count, 'Std_Dev_Match_Counts': std_dev_match_count})

    df = pd.DataFrame(results)
    df.to_csv(output_file, index=False)
    print(f"Data saved to: {output_file}")

if __name__ == '__main__':
    main()
