import torch
import model
from data_loader import SampleLevelMTTDataset
import argparse
import model
from solver import Solver

parser = argparse.ArgumentParser()
parser.add_argument('--gpus', nargs='+', type=int, default=[])
parser.add_argument('--train', action='store_true')
parser.add_argument('--test', action='store_true')
args = parser.parse_args()

print("gpu devices being used: ", args.gpus)


def main():
    
    if args.train or args.test:
        dataset = SampleLevelMTTDataset()
        samplecnn = model.SampleCNN()
        mysolver = Solver(samplecnn, dataset, args)
    else:
        print("Nothing to be done...")

    if args.train:
        # start training
        print("Start training!!")
        mysolver.train()
        print("Finished! Hopefully..")

    if args.test:
        # test it
        print("Start testing...")
        mysolver.eval('test')


if __name__ == '__main__':
    main()

