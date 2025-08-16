class FormChecker:
    def check(self, landmarks, exercise="Squats"):
        if landmarks is None:
            return "No person detected"

        if exercise=="Squats" or exercise=="Lunges":
            l_shoulder = [landmarks.landmark[11].x, landmarks.landmark[11].y]
            r_shoulder = [landmarks.landmark[12].x, landmarks.landmark[12].y]
            l_hip = [landmarks.landmark[23].x, landmarks.landmark[23].y]
            r_hip = [landmarks.landmark[24].x, landmarks.landmark[24].y]
            torso_slope = abs((l_shoulder[1]+r_shoulder[1])/2 - (l_hip[1]+r_hip[1])/2)
            if torso_slope < 0.05:
                return "Back too bent"
            return "Good form"

        elif exercise=="Push-ups":
            # torso flat check
            l_shoulder = landmarks.landmark[11].y
            r_shoulder = landmarks.landmark[12].y
            l_hip = landmarks.landmark[23].y
            r_hip = landmarks.landmark[24].y
            slope = abs((l_shoulder+r_shoulder)/2 - (l_hip+r_hip)/2)
            if slope > 0.1:
                return "Hips too low/high"
            return "Good form"

        elif exercise=="Jumping Jacks":
            return "Form OK"

        return "Good form"
