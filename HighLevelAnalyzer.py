# Settings constants.
from saleae.analyzers import HighLevelAnalyzer, AnalyzerFrame, StringSetting, NumberSetting, ChoicesSetting
from saleae.data import GraphTimeDelta
import json

class Hla(HighLevelAnalyzer):

    result_types = {
            'summary': {
                'format': '{{data.input_type}}: {{data.summary}}'
            }
        }

    def __init__(self):
        pass

    def decode(self, frame):
        data_copy = {}
        for key in frame.data:
            value = frame.data[key]
            if type(value) is bytes:
                data_copy[key] = [x for x in value]
            else:
                data_copy[key] = value

        summary = json.dumps(data_copy, indent=0, separators=(', ', ': ')).replace("\n", "").replace("\"", "")
        print(summary)

        # Return the data frame itself
        return AnalyzerFrame('summary', frame.start_time, frame.end_time, {
                'input_type': frame.type,
                'summary': summary
        })
