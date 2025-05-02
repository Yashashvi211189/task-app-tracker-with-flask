<h1 align="center">DevOps Backend Project</h1>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.9-blue" alt="Python Version">
  <img src="https://img.shields.io/badge/flask-2.3-green" alt="Flask Version">
  <img src="https://img.shields.io/badge/docker-%3E%3D20.10-blue" alt="Docker Version">
</p>

<div align="center">
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" width="100" alt="Docker">
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original-wordmark.svg" width="100" alt="Python">
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/flask/flask-original-wordmark.svg" width="100" alt="Flask">
</div>

<h2>🚀 Features</h2>
<ul>
  <li>Task management system (CRUD operations)</li>
  <li>Docker containerization</li>
  <li>SQLite database integration</li>
  <li>Modern box-based UI</li>
  <li>Health check endpoints</li>
</ul>

<h2>📦 Installation</h2>
<pre><code># Clone the repository
git clone https://github.com/YOUR-USERNAME/my-devops-projectbackend.git
cd my-devops-projectbackend

# Build and run with Docker
docker-compose up -d --build
</code></pre>

<h2>🛠️ Development</h2>
<pre><code># Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\Activate

# Install dependencies
pip install -r requirements.txt

# Run the application
flask run --host=0.0.0.0 --port=8000
</code></pre>

<h2>🌐 Access</h2>
<p>The application will be available at:</p>
<ul>
  <li>Main Page: <code>http://localhost:8000</code></li>
  <li>Task Manager: <code>http://localhost:8000/tasks</code></li>
  <li>Health Check: <code>http://localhost:8000/check-status</code></li>
</ul>

<h2>📂 Project Structure</h2>
<pre>
my-devops-projectbackend/
├── app.py                # Main application
├── Dockerfile            # Production container setup
├── docker-compose.yml    # Development environment
├── requirements.txt      # Python dependencies
├── static/               # CSS/JS files
│   ├── styles.css
│   └── script.js
└── templates/            # HTML templates
    ├── index.html
    ├── tasks.html
    └── about.html
</pre>

<h2>📜 License</h2>
<p>MIT License</p>

<div align="center">
  <p>Built with ❤️ by <YOUR-NAME></p>
</div>
