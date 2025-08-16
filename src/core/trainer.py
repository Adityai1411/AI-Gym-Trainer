from .pose_estimator import PoseEstimator
from .rep_counter import RepCounter
from .form_checker import FormChecker

class Trainer:
    def __init__(self):
        self.pose = PoseEstimator()
        self.counter = RepCounter()
        self.form = FormChecker()

    def process(self, frame):
        keypoints = self.pose.estimate(frame)
        reps = self.counter.update(keypoints)
        feedback = self.form.check(keypoints)
        return reps, feedback
