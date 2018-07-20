from flask import Flask
import plivo, plivoxml
import os

port = int(os.getenv('PORT', 8000))

app = Flask(__name__)

@app.route('/text-to-speech/<stan>', methods=['GET','POST'])
def speak_xml(stan):
    # Generate a Speak XML with the details of the text to play on the call.
    r = plivoxml.Response()

    # Add Speak XML Tag with English text
    body1 = '%s'%stan
    params1 = {
        'language': "en-GB", # Language used to read out the text.
        'voice': "WOMAN" # The tone to be used for reading out the text.
    }
    r.addSpeak(body1, **params1)
    print (r.to_xml)
    return Response(str(r), mimetype='text/xml')
		
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port, debug=True)