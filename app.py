from flask import Flask, render_template, jsonify, request
import os
import json
from pathlib import Path

app = Flask(__name__)

# Path to the outputs folder
OUTPUTS_FOLDER = Path("research_assistant/outputs")

@app.route('/')
def index():
    """Home page that lists all JSON files"""
    json_files = []
    
    if OUTPUTS_FOLDER.exists():
        for file in OUTPUTS_FOLDER.glob("*.json"):
            # Get file stats
            stat = file.stat()
            
            # Try to extract paper title from JSON
            paper_title = file.name  # Default to filename if title extraction fails
            try:
                with open(file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if 'bibliographic_metadata' in data and 'title' in data['bibliographic_metadata']:
                        paper_title = data['bibliographic_metadata']['title']
            except Exception:
                # If there's any error reading the JSON, keep the filename
                pass
            
            json_files.append({
                'name': file.name,
                'title': paper_title,
                'size': f"{stat.st_size / 1024:.1f} KB",
                'modified': stat.st_mtime
            })
    
    # Sort by title
    json_files.sort(key=lambda x: x['title'])
    
    return render_template('index.html', files=json_files)

@app.route('/view/<filename>')
def view_file(filename):
    """View the contents of a specific JSON file"""
    file_path = OUTPUTS_FOLDER / filename
    
    if not file_path.exists() or not filename.endswith('.json'):
        return "File not found", 404
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        return render_template('view.html', filename=filename, data=data)
    
    except Exception as e:
        return f"Error reading file: {str(e)}", 500

@app.route('/api/file/<filename>')
def get_file_data(filename):
    """API endpoint to get JSON file data"""
    file_path = OUTPUTS_FOLDER / filename
    
    if not file_path.exists() or not filename.endswith('.json'):
        return jsonify({'error': 'File not found'}), 404
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        return jsonify(data)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 