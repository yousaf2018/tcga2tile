import os
import argparse

from code.tile_factory import TileFactory
import os
import shutil
import pandas as pd


df = pd.read_csv("/kaggle/working/tcga2tile/exists.csv")

def get_parser():
    parser = argparse.ArgumentParser(description='Data preprocessing module: sampling tiles from slide')
    parser.add_argument('--tile-size', type=int, default=256,
                        help='width/height of tiles.')
    parser.add_argument('--overlap', type=str, default=None,
                        help='overlap of tiles.')
    parser.add_argument('--slide-file', type=str, default=None,
                        help='path of <has_been_downloaded> file.')
    parser.add_argument('--num-workers', type=str, default=8,
                        help='num of process for cropping slide.')
    parser.add_argument('--output_path', type=str, default=None,
                        help='path to save the tiles.')
    parser.add_argument('--start', type=int, default=None,
                        help='counter for total wsi to process')
    parser.add_argument('--end', type=int, default=None,
                        help='counter for total wsi to process')
    return parser


def main(args):
    print(args, args.__dict__)
    folder_path = args.slide_file
    folder_path_out = args.output_path
    # Iterate through all items in the folder
    counter = 0

    for root, dirs, files in os.walk("/kaggle/input/tcga-wsi-svs"):
        for file in files:
            # print(file)   
            if counter == 0:
                pass
            else:
                if file.endswith(".svs") and file.split(".svs")[0] not in df["PATIENT"].values:
                    print(counter)
                    # print(os.path.join(root, file))
                    tile_factory = TileFactory(os.path.join(root, file), args.tile_size, args.overlap, output_path=args.output_path,
                                            num_workers=args.num_workers)
                    tile_factory.make_overview()
                    tile_factory.make_tiles()
                    counter += 1
            counter+=1



if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    main(args)
