from flask import Flask, render_template, request, jsonify, make_response
from shortest import calculate_shortest
from quietest import calculate_quietest
import time 
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_coordinates', methods=['POST'])
def process_coordinates():
    data = request.get_json()
    start_coords = data.get('start_coords')
    end_coords = data.get('end_coords')
    mode = data.get('mode')
    print(mode,start_coords, end_coords)
    if mode == 'shortest':
        calculate_shortest(start_coords, end_coords)
        time.sleep(3)
        return render_template('shortest.html')  # Render the shortest.html template
    elif mode == 'quietest':
        calculate_quietest(start_coords, end_coords)
        time.sleep(3)
        return render_template('quietest.html')  # Render the quietest.html template
    else:
        return jsonify({'error': 'Invalid mode'})
    
@app.route('/quietest.html')  # Route to serve quietest.html
def serve_quietest():
    response = make_response(render_template('quietest.html'))
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/shortest.html')  # Route to serve shortest.html
def serve_shortest():
    response = make_response(render_template('shortest.html'))
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

if __name__ == '__main__':
    app.run(debug=True)
