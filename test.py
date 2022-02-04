import unittest
from main import SurvivePredictor, PersonInformation

class TestClassifier(unittest.TestCase):
    """
    Allows to test the classifier
    Args:
        unittest.Testcase: [description]
    """
    def test_classifier(self):
        """a simple test implemented to test predictions of the classifier
        """
        self.predictor = SurvivePredictor()
        assert 0.5 > self.predictor.predict(
            PersonInformation(sex='male', pclass=2)), "Issue with prediction negative"
        assert 0.5 < self.predictor.predict(
            PersonInformation(sex='female', pclass=2)), "Issue with prediction positive"
    
        

if __name__ == '__main__':
    unittest.main()