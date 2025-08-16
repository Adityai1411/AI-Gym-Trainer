import math

class RepCounter:
    def __init__(self):
        self.count = 0
        self.stage = None  # "down" or "up"

    def calculate_angle(self, a, b, c):
        radians = math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0])
        angle = abs(radians * 180.0 / math.pi)
        if angle > 180.0:
            angle = 360 - angle
        return angle

    def update(self, landmarks, exercise="Squats"):
        if landmarks is None:
            return self.count

        if exercise == "Squats" or exercise=="Lunges":
            # Left leg
            l_hip = [landmarks.landmark[23].x, landmarks.landmark[23].y]
            l_knee = [landmarks.landmark[25].x, landmarks.landmark[25].y]
            l_ankle = [landmarks.landmark[27].x, landmarks.landmark[27].y]
            angle_left = self.calculate_angle(l_hip, l_knee, l_ankle)

            # Right leg
            r_hip = [landmarks.landmark[24].x, landmarks.landmark[24].y]
            r_knee = [landmarks.landmark[26].x, landmarks.landmark[26].y]
            r_ankle = [landmarks.landmark[28].x, landmarks.landmark[28].y]
            angle_right = self.calculate_angle(r_hip, r_knee, r_ankle)

            avg_knee_angle = (angle_left + angle_right) / 2

            if avg_knee_angle < 90:
                self.stage = "down"
            if avg_knee_angle > 160 and self.stage == "down":
                self.stage = "up"
                self.count += 1

        elif exercise == "Push-ups":
            # elbows/shoulder logic
            l_shoulder = [landmarks.landmark[11].x, landmarks.landmark[11].y]
            l_elbow = [landmarks.landmark[13].x, landmarks.landmark[13].y]
            l_wrist = [landmarks.landmark[15].x, landmarks.landmark[15].y]
            angle_left = self.calculate_angle(l_shoulder, l_elbow, l_wrist)

            r_shoulder = [landmarks.landmark[12].x, landmarks.landmark[12].y]
            r_elbow = [landmarks.landmark[14].x, landmarks.landmark[14].y]
            r_wrist = [landmarks.landmark[16].x, landmarks.landmark[16].y]
            angle_right = self.calculate_angle(r_shoulder, r_elbow, r_wrist)

            avg_elbow_angle = (angle_left + angle_right)/2

            if avg_elbow_angle < 90:
                self.stage = "down"
            if avg_elbow_angle > 160 and self.stage=="down":
                self.stage="up"
                self.count+=1

        elif exercise == "Jumping Jacks":
            # Simplified: count by hands up
            l_shoulder = landmarks.landmark[11].y
            r_shoulder = landmarks.landmark[12].y
            if l_shoulder < 0.3 and r_shoulder < 0.3:
                self.stage = "up"
            elif l_shoulder > 0.5 and r_shoulder > 0.5 and self.stage=="up":
                self.count+=1
                self.stage="down"

        return self.count
