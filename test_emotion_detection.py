"""
Unit testing for Emotion Detection application
"""

import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_joy_emotion(self):
        result = emotion_detector("I am very happy today!")
        self.assertIn("joy", result)

    def test_sad_emotion(self):
        result = emotion_detector("I am feeling very sad.")
        self.assertIn("sadness", result)

    def test_anger_emotion(self):
        result = emotion_detector("I am extremely angry.")
        self.assertIn("anger", result)

    def test_fear_emotion(self):
        result = emotion_detector("I am scared of the dark.")
        self.assertIn("fear", result)

    def test_disgust_emotion(self):
        result = emotion_detector("This is disgusting.")
        self.assertIn("disgust", result)


if __name__ == "__main__":
    unittest.main()
