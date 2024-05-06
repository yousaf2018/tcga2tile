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
    parser.add_argument('--num-workers', type=str, default=4,
                        help='num of process for cropping slide.')
    parser.add_argument('--output_path', type=str, default=None,
                        help='path to save the tiles.')
    return parser


def main(args):
    print(args, args.__dict__)
    # folder_path = args.input_path
    # folder_path_out = args.output_path
    # # Iterate through all items in the folder
    # counter = 0
    # for item in os.listdir(folder_path):
    #     item_path = os.path.join(folder_path, item)
        
    #     # Check if it's a directory
    #     if os.path.isdir(item_path):
    #         # Get the name of the SVS file inside the directory
    #         svs_files = [f for f in os.listdir(item_path) if f.endswith('.svs')]
    #         if svs_files:
    #             svs_file = svs_files[0]
    #             print(svs_file)
    tile_factory = TileFactory(args.slide_file, args.tile_size, args.overlap, output_path=args.output_path,
                            num_workers=args.num_workers)
    tile_factory.make_overview()
    tile_factory.make_tiles()


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    main(args)
