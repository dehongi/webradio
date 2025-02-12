# Django Online Radio

A simple web-based radio application built with Django and Django Channels that allows users to upload and stream audio tracks synchronously across multiple clients.

## Features

- Upload audio tracks with artist and title information
- Live streaming functionality using WebSocket
- Synchronized playback across all connected clients
- Real-time "Now Playing" updates
- Simple and responsive Bootstrap UI
- Admin interface for track management

## Prerequisites

- Python 3.8+
- Django 5.1+
- Django Channels
- A modern web browser with HTML5 audio support

## Installation

1. Clone the repository:

```bash
git clone https://github.com/dehongi/webradio.git
cd webradio
```

2. Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

3. Apply database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

4. Create a superuser account:

```bash
python manage.py createsuperuser
```

5. Run the development server:

```bash
python manage.py runserver
```

6. Open your web browser and navigate to `http://localhost:8000` to access the radio application.

## Usage

### For Users

1. **Browse Tracks**
   - Visit the home page to see all available tracks
   - View currently playing track in the "Now Playing" section
   - Click "Play on Radio" to start playing a track for all listeners

2. **Upload New Tracks**
   - Click "Upload Track" in the navigation bar
   - Fill in the track details (title and artist)
   - Select an audio file from your computer
   - Click "Upload" to add the track to the library

### For Administrators

1. Access the admin interface at `http://localhost:8000/admin`
2. Log in with your superuser credentials
3. Manage tracks, users, and other site content

## Project Structure

```
webradio/
├── django_project/          # Project configuration
│   ├── settings.py        # Project settings
│   ├── urls.py           # Main URL configuration
│   └── asgi.py           # ASGI configuration for WebSocket
├── radio/                  # Main application
│   ├── templates/        # HTML templates
│   │   ├── base.html    # Base template
│   │   ├── track_list.html
│   │   └── track_form.html
│   ├── models.py         # Track model
│   ├── views.py          # View controllers
│   ├── urls.py          # App URL patterns
│   ├── consumers.py     # WebSocket consumer
│   └── routing.py       # WebSocket routing
└── manage.py             # Django management script
```

## Technical Implementation

### Models

```python
class Track(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    audio_file = models.FileField(upload_to="tracks/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_playing = models.BooleanField(default=False)
```

### WebSocket Integration

- Uses Django Channels for real-time communication
- Implements an async consumer for handling WebSocket connections
- Broadcasts track changes to all connected clients
- Synchronizes playback across multiple browsers

### File Storage

- Audio files are stored in the `media/tracks/` directory
- Served through Django's media file handling
- Supports common audio formats (MP3, WAV, etc.)

## Development

To contribute to this project:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/NewFeature`)
3. Make your changes
4. Commit (`git commit -m 'Add NewFeature'`)
5. Push to the branch (`git push origin feature/NewFeature`)
6. Create a Pull Request

## Troubleshooting

Common issues and solutions:

1. **WebSocket Connection Failed**
   - Ensure Django Channels is properly installed
   - Check if the ASGI application is configured correctly
   - Verify the WebSocket URL in the template

2. **Audio Files Not Playing**
   - Check if the media files are properly uploaded
   - Verify media URL configuration in settings.py
   - Ensure the browser supports the audio format

3. **Database Migrations**
   - Run `python manage.py makemigrations` followed by `python manage.py migrate`
   - Check for any pending migrations

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- Django framework and community
- Django Channels documentation
- Bootstrap for the UI components
- All contributors and users of this project
