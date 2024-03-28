import time
import numpy as np
import argparse



def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='Occupy CPU and memory')
    parser.add_argument('--duration',
                        type=int,
                        default=100,
                        help='Duration of the run (s).')
    parser.add_argument('--cpu_m_size',
                        type=int,
                        default=100,
                        help='Size of n*n matrix')
    parser.add_argument('--cpu_m_freq',
                        type=int,
                        default=100,
                        help='number of multiplication')
    parser.add_argument('--mem_m_freq',
                        type=int,
                        default=1000,
                        help='Number of objects in memory list')
    parser.add_argument('--mem_m_size',
                        type=int,
                        default=1000,
                        help='Size of n by n matrix')
    return parser.parse_args()


def occupy_resources(duration, cpu_m_size, cpu_m_freq, mem_m_size, mem_m_freq):

    print('Running occupy resources')
    
    # Duration in seconds
    end_time = time.time() + duration

    # Occupying CPU
    while time.time() < end_time:
        _ = [np.random.rand(cpu_m_size, cpu_m_size) for _ in range(cpu_m_freq)]

        # Occupying memory by growing a list
        memory_occupier = []
        for _ in range(mem_m_freq):
            memory_occupier.append(np.random.rand(mem_m_size, mem_m_size))
            if time.time() >= end_time:
                break

        del memory_occupier

def main():
    args = parse_args()
    occupy_resources(args.duration,
                     args.cpu_m_size,
                     args.cpu_m_freq,
                     args.mem_m_size,
                     args.mem_m_freq)

if __name__ == "__main__":
    main()
