import json
import argparse
import csv
from random import choices

# You should run:
# e.g. `python eval_data/quick_visualize.py --src dec_15_stage3`

feats = [
    "image_path",
    "size",
    "shape",
    "equator",
    "lateral_slopes",
    "poles",
    "length",
    "width",
    "ratio",
    "axis_shape",
    "number_of_volutions",
    "coil_tightness",
    "height_of_volution",
    "thickness_of_spirotheca",
    "septa",
    "proloculus",
    "tunnel_angles",
    "tunnel_shape",
    "chomata",
    "axial_filling"
]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--src", help="src folder")
    
    args = parser.parse_args()
    src:str = args.src
    with open(f'eval_data/qwen3_eval/{src}/extracted_output_info.json', 'r') as f:
        output_info = json.load(f)
    
    with open(f'eval_data/qwen3_eval/{src}/extracted_output_info.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(feats)
        for res in output_info:
            writer.writerow([res[feat] for feat in feats])
    
    with open(f"eval_data/origin_files/{src}.json", 'r') as f:
        origin_info = json.load(f)
    samples = choices(origin_info, k=5)

    with open(f'eval_data/qwen3_eval/{src}/samples.md', 'w') as f:
        f.write("# Sampled Images:\n")
        for sample in samples:
            f.write(f'![{sample["img"]}](/home/nfs05/xiangch/geocap/dataset/common/images/{sample["img"]})')
            f.write('\n')
            f.write(f'## Question:\n')
            f.write(sample["question"])
            f.write('\n')
            f.write(f'## Output:\n')
            f.write(sample['output'])
            f.write('\n')
            f.write(f'## Ground Truth:\n')
            f.write(sample['reference'])
            f.write('\n')
    
    


    
if __name__ == "__main__":
    main()