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
        <meta property="fc:frame:image" content="http://example.com/poll_image.png" />
        <meta property="fc:frame:button:1" content="Option 1" />
        <meta property="fc:frame:button:2" content="Option 2" />
        <!-- Add more buttons as needed -->
    </head>
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
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><link rel="preload" href="/_next/static/media/ec1a1eae803b668e-s.p.woff2" as="font" crossorigin="" type="font/woff2"><link rel="preload" as="image" href="/api/image?id=054aee65-c63d-46c1-a1f9-a05b747860f6&amp;results=true&amp;date=1706869377506"><link rel="stylesheet" href="/_next/static/css/3de5de1d4f958ee2.css" data-precedence="next"><link rel="preload" as="script" fetchpriority="low" href="/_next/static/chunks/webpack-221f8c6f61fdc45f.js"><script src="/_next/static/chunks/fd9d1056-f315ea3758789158.js" async=""></script><script src="/_next/static/chunks/69-d38673478e033ebc.js" async=""></script><script src="/_next/static/chunks/main-app-f5c8d25c8479457f.js" async=""></script><script src="/_next/static/chunks/app/polls/%5Bid%5D/page-4d4342986485a75c.js" async=""></script><title>Test</title><meta name="fc:frame" content="vNext"><meta name="fc:frame:post_url" content="https://fc-polls.vercel.app/api/vote?id=054aee65-c63d-46c1-a1f9-a05b747860f6"><meta name="fc:frame:image" content="https://fc-polls.vercel.app/api/image?id=054aee65-c63d-46c1-a1f9-a05b747860f6"><meta name="fc:frame:button:1" content="1"><meta name="fc:frame:button:2" content="2"><meta name="fc:frame:button:3" content="3"><meta name="fc:frame:button:4" content="4"><meta property="og:title" content="Test"><meta property="og:image" content="https://fc-polls.vercel.app/api/image?id=054aee65-c63d-46c1-a1f9-a05b747860f6"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="Test"><meta name="twitter:image" content="https://fc-polls.vercel.app/api/image?id=054aee65-c63d-46c1-a1f9-a05b747860f6"><link rel="icon" href="/favicon.ico" type="image/x-icon" sizes="16x16"><meta name="next-size-adjust"><script src="/_next/static/chunks/polyfills-c67a75d1b6f99dc8.js" nomodule=""></script></head>
        </html>
        '''.format(new_image_url)
        return updated_html_content
    else:
        return jsonify({'error': 'Invalid message'}), 400

if __name__ == '__main__':
    app.run(debug=True)

