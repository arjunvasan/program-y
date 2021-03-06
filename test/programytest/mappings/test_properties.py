import unittest
from programy.mappings.properties import PropertiesCollection

class PropertysTests(unittest.TestCase):

    def test_properties_from_text(self):

        properties = PropertiesCollection()
        self.assertIsNotNone(properties)

        properties.load_from_text("""
            url:http://www.keithsterling.com/aiml
            name:KeiffBot 1.0
            firstname:Keiff
            middlename:AIML
            lastname:BoT
            fullname:KeiffBot
            email:info@alicebot.org
            gender:male
            botmaster:Keith Sterling
            organization:keithsterling.com
            version:0.0.1
            birthplace:Edinburgh, Scotland
            job:mobile virtual assistant
            species:robot
            birthday:September 9th
            birthdate:September 9th, 2016
            sign:Virgo
            logo:<img src="http://www.keithsterling.com/aiml/logo.png" width="128"/>
            religion:Atheist
            default-get:unknown
            default-property:unknown
            default-map:unknown
            learn-filename:keiffbot-learn.aiml
        """)

        self.assertEqual(properties.property('url'), "http://www.keithsterling.com/aiml")
        self.assertEqual(properties.property('job'), "mobile virtual assistant")
        self.assertEqual(properties.property('learn-filename'), "keiffbot-learn.aiml")