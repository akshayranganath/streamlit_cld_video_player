from pathlib import Path
from typing import Optional

import streamlit as st
import streamlit.components.v1 as components

# Tell streamlit that there is a component called streamlit_cld_video_player,
# and that the code to display that component is in the "frontend" folder
frontend_dir = (Path(__file__).parent / "frontend").absolute()
_component_func = components.declare_component(
	"cld_video_player", path=str(frontend_dir)
)

# Create the python function that will be called
def cld_video_player(
        cloud_name: str,
        public_id: str,
        aiHighlightsGraph: bool = False,
        bigPlayButton: bool = False,
        controls: bool = True,
        loop: bool = False,
        muted: bool = True,
        playsinline: bool = False,
        fluid: bool = True,
        showinfo: bool = True,
        showLogo: bool = True,           
        startAt: int = 0,
        autoplay: bool = False,
        autoplayMode: str = 'on-scroll',
        pictureInPictureToggle: bool = False,        
        title: str = 'Video Title',
        subtitle: str = 'Video Subtitle',
        skin: str = 'dark',
        key: Optional[str] = None
):
    """
    Add a descriptive docstring
    """
    component_value = _component_func(
        cloud_name = cloud_name,
        public_id = public_id,
        aiHighlightsGraph = aiHighlightsGraph,
        bigPlayButton = bigPlayButton,
        controls = controls,
        loop = loop,
        muted = muted,
        playsinline = playsinline,
        fluid = fluid,
        showinfo = showinfo,
        showLogo = showLogo,        
        startAt = startAt,
        autoplay = autoplay,
        autoplayMode = autoplayMode,
        pictureInPictureToggle = pictureInPictureToggle,        
        title = title,
        subtitle = subtitle,
        skin = skin,
        key = key
    )

    return component_value

def main():
    st.write("## Sample Video Player by Cloudinary")
    value = cld_video_player(
        cloud_name='demo',
        public_id='dog'                
        )

if __name__ == "__main__":
    main()
