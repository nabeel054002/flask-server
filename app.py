from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World!'

@app.route('/poll', methods=['GET'])
def poll_frame():
    # HTML content with Open Graph tags for the poll frame
    html_content = '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta property="fc:frame" content="vNext" />
        <meta property="fc:frame:image" content="https://drive.google.com/file/d/1zewPIpVfgQioCwPZdyzsWJPjsJtWn5hP/view?usp=sharing" />
        <meta property="fc:frame:button:1" content="Green" />
        <meta property="fc:frame:button:2" content="Purple" />
        <meta property="fc:frame:button:3" content="Red" />
        <meta property="fc:frame:button:4" content="Blue" />
        <meta property="og:image" content="https://drive.google.com/file/d/1rZRQyrAm2DgSq88aYCreHO4kADtTvzfU/view?usp=sharing"/>
    </head>
    <body></body>
    </html>
    '''
    return html_content

@app.route('/poll', methods=['POST'])
def process_poll():
    # Logic to handle the poll response
    # Extract the signed message from the request
    signed_message = request.json.get('signedMessage')

    # Validate the signed message with Farcaster Hub (placeholder URL)
    validate_url = 'https://farcaster_hub/validateMessage'
    response = requests.post(validate_url, json={'message': signed_message})

    if response.status_code == 200:
        # Generate updated results image (placeholder logic)
        new_image_url = 'http://example.com/updated_poll_image.png'

        # Return the updated frame with new image
        updated_html_content = '''
        <!DOCTYPE html>
        <html>
        <head><meta charset="utf-8"><meta name="viewport" content="width=device-width"><meta property="og:title" content="Frame"><meta property="fc:frame" content="vNext"><meta property="fc:frame:button:1" content="Choose Their Fate"><meta property="og:image" content="undefined/start.png"><meta property="fc:frame:image" content="undefined/start.png"><meta property="fc:frame:post_url" content="undefined/api/post?slide=1"><meta name="next-head-count" content="8"><noscript data-n-css=""></noscript><script defer="" crossorigin="" nomodule="" src="/_next/static/chunks/polyfills-c67a75d1b6f99dc8.js"></script><script src="/_next/static/chunks/webpack-ee7e63bc15b31913.js" defer="" crossorigin=""></script><script src="/_next/static/chunks/framework-5429a50ba5373c56.js" defer="" crossorigin=""></script><script src="/_next/static/chunks/main-930135e47dff83e9.js" defer="" crossorigin=""></script><script src="/_next/static/chunks/pages/_app-b8840b4f8f2fad1f.js" defer="" crossorigin=""></script><script src="/_next/static/chunks/pages/index-016a53a5b212a55f.js" defer="" crossorigin=""></script><script src="/_next/static/51hnj2FBt_qAUyFWtCs7G/_buildManifest.js" defer="" crossorigin=""></script><script src="/_next/static/51hnj2FBt_qAUyFWtCs7G/_ssgManifest.js" defer="" crossorigin=""></script></head>
        <body></body>
        </html>
        '''.format(new_image_url)
        return updated_html_content
    else:
        return jsonify({'error': 'Invalid message'}), 400

if __name__ == '__main__':
    app.run(debug=True)

