import argparse
from typing import Any, List
import random
from quick_test_py import Tester
import os

from common_ml.model import FrameModel
from common_ml.tags import FrameTag

test_file = os.path.join(os.path.dirname(__file__), 'test.mp4')

class FakeFrameModel(FrameModel):
    def tag(self, img: Any) -> List[FrameTag]:
        return self.random_tag()

    def random_tag(self) -> List[FrameTag]:
        num_tags = random.randint(1, 3)
        return [FrameTag(f"fake{random.randint(1, 10)}", (0.5, 0.95, 0.95, 0.5)) for _ in range(num_tags)]
    
def test_tag():
    random.seed(42)
    model = FakeFrameModel()
    t1 = lambda: model.tag_video(test_file, False, 1)
    t2 = lambda: model.tag_video(test_file, True, 1)
    t3 = lambda: model.tag_video(test_file, False, 2)
    t4 = lambda: model.tag_video(test_file, True, 2)
    return [t1, t2, t3, t4]
    
def main():
    tester = Tester(os.path.dirname(__file__) + '/test_data')
    tester.register('test_tag', test_tag())
    if args.record:
        tester.record()
    else:
        tester.validate()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--record', action='store_true')
    args = parser.parse_args()
    main()