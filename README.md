# streamlit_cld_video_player

Embed Cloudinary's [video player](https://cloudinary.com/documentation/cloudinary_video_player) as a component in Streamlit applications.

## Installation instructions 

```sh
pip install streamlit_cld_video_player
```

## Usage instructions

```python
import streamlit as st

from streamlit_cld_video_player import cld_video_player

value = cld_video_player(
    cloud_name='demo', # your environment name on Cloudinary
    public_id='dog' # name of a video file on Cloudinary
)

st.write(value)
```

## Detailed Usage

Upload widget is the tool used for embedding Cloudinary's Upload Widget into your application. The widget has quite a few customization parameters. This python module exposes the following options:

Video player widget is a tool used for embedding Cloudinary's Video Player widget into your applications. The widget has 4 types of configuration parameters listed on the [Video Player API reference](https://cloudinary.com/documentation/video_player_api_reference) page. However, for this python implementation, we can configure the following parameters:

| Parameter              | Purpose                                                                                                                                               | Default Value        |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| cloud_name             | Name of your Cloudinary product environment                                                                                                           | None. Required value |
| public_id              | Name of your video.                                                                                                                                   | None. Required value |
| aiHighlightsGraph      | Show an AI-generated visual representation of the highlights of a video                                                                    | FALSE                |
| bigPlayButton          | Show a larger central play button when the video is paused.                                                                                | FALSE                |
| controls               | Display the video player controls                                                                                                          | TRUE                 |
| loop                   | Perform standard HTML5 video looping.                                                                                                      | FALSE                |
| muted                  | Start the video muted.                                                                                                                     | TRUE                 |
| playsinline            | Relevant for iOS only. Whether the video should be prevented from entering fullscreen mode automatically when playback begins.                        | FALSE                |
| fluid                  | Whether to activate fluid layout mode, which dynamically adjusts the player size to fit its container or window.                                      | TRUE                 |
| showinfo               | Display the video information like the title and subtitle of the video. The values are provided with the parameters "title" and "subtitle" | TRUE                 |
| showLogo               | Show a clickable logo within the player.                                                                                                   | TRUE                 |
| startAt                | Time at which to start the video playback.                                                                                                            | 0                    |
| autoplay               | Apply standard HTML5 autoplay.                                                                                                             | FALSE                |
| autoplayMode           | The autoplay mode to use for the player. Similar to the default HTML5 autoplay parameter, but with the addition of on-scroll support.                 | on-scroll            |
| pictureInPictureToggle | Show the picture in picture toggle button.                                                                                                 | FALSE                |
| title                  | Title to be displayed for the video                                                                                                                   | NONE                 |
| subtitle               | Subtitle to be displayed for the video                                                                                                                | NONE                 |
| skin                   | Use the 'light' or 'dark' mode.                                                                                                            | dark'                |