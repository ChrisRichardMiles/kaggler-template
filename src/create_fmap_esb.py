import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--base-models', required=True, nargs='+', dest='base_models')
    parser.add_argument('--feature-header-file', required=True, dest='feature_header_file')

    args = parser.parse_args()

    with open(args.feature_header_file, 'w') as f:
        for i, col in enumerate(args.base_models):
            f.write(f'{col}\n')
