import os
import argparse

from code.tile_factory import TileFactory
import os
import shutil




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
    return parser


def main(args):
    print(args, args.__dict__)
    folder_path = args.slide_file
    folder_path_out = args.output_path
    # Iterate through all items in the folder
    counter = 0

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".svs"):
                tile_factory = TileFactory(os.path.join(root, file), args.tile_size, args.overlap, output_path=args.output_path,
                                        num_workers=args.num_workers)
                tile_factory.make_overview()
                tile_factory.make_tiles()


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    main(args)
