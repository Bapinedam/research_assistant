# Research Data Viewer - Flask Web Application

A modern, responsive web application built with Flask to browse and view research JSON files from your outputs folder.

## Features

- 📁 **File Browser**: Lists all JSON files from the `research_assistant/outputs` folder
- 👁️ **Content Viewer**: Displays JSON content in an organized, readable format
- 📱 **Responsive Design**: Works on desktop and mobile devices
- 🎨 **Modern UI**: Beautiful gradient design with smooth animations
- 🔍 **Interactive Sections**: Collapsible sections for better navigation
- 📊 **File Information**: Shows file size and modification details
- 💻 **Raw JSON View**: Access to the original JSON format

## Installation

1. **Install Flask dependencies**:
   ```bash
   pip install -r requirements_flask.txt
   ```

2. **Run the application**:
   ```bash
   python app.py
   ```

3. **Access the web application**:
   Open your browser and go to: `http://localhost:5000`

## File Structure

```
Research Project/
├── app.py                          # Main Flask application
├── templates/                      # HTML templates
│   ├── base.html                   # Base template with styling
│   ├── index.html                  # File list page
│   └── view.html                   # JSON content viewer
├── research_assistant/
│   └── outputs/                    # JSON files to display
│       ├── 2401.04122v3.json
│       ├── 2402.01386v1.json
│       └── ... (other JSON files)
└── requirements_flask.txt          # Flask dependencies
```

## Usage

1. **Home Page**: The main page shows all available JSON files with their sizes
2. **View Content**: Click on any file to see its organized content
3. **Navigation**: Use the "Back to File List" button to return to the main page
4. **Expand/Collapse**: Use the buttons to expand or collapse all sections
5. **Raw JSON**: Scroll down to see the original JSON format

## JSON Structure Support

The application is designed to handle research paper metadata with sections like:
- Bibliographic Metadata
- Methodological Framework
- Technical Pipeline
- Prompt Engineering
- Empirical Results
- Quality Assurance
- Research Impact

## Customization

- **Styling**: Modify the CSS in `templates/base.html`
- **Layout**: Edit the HTML templates in the `templates/` folder
- **Functionality**: Add new routes in `app.py`

## Troubleshooting

- **No files shown**: Make sure JSON files exist in `research_assistant/outputs/`
- **Port already in use**: Change the port in `app.py` (line 58)
- **File not found errors**: Check file permissions and paths

## Development

To run in development mode with auto-reload:
```bash
export FLASK_ENV=development
python app.py
```

The application will automatically reload when you make changes to the code. 