import streamlit as st
from PIL import Image
# Note: OpenCV (cv2) is optional. Remove the import to avoid deployment issues unless you add
# `opencv-python` to your `requirements.txt` and your deployment environment supports it.
import base64
import os

# Display logo (centered and resized to one-quarter of original dimensions)
def _set_background_glass(img_path: str = "ugb1.png"):
    """Set a full-page background using the given image and add a translucent glass
    style to the main Streamlit block container so content appears on a frosted panel.
    The image is embedded as a data URI to improve compatibility when deployed.
    """
    try:
        if not os.path.exists(img_path):
            return
        with open(img_path, "rb") as f:
            data = f.read()
        b64 = base64.b64encode(data).decode()
        css = f"""
        <style>
        .stApp {{
            /* Apply a white overlay so the image appears very subtle, requiring focus to notice */
            background-image: linear-gradient(rgba(255,255,255,0.92), rgba(255,255,255,0.92)), url("data:image/png;base64,{b64}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        .stApp .main .block-container {{
            background: rgba(255,255,255,0.6);
            backdrop-filter: blur(6px);
            -webkit-backdrop-filter: blur(6px);
            border-radius: 12px;
            padding: 1rem 1.5rem;
        }}
        </style>
        """
        st.markdown(css, unsafe_allow_html=True)
    except Exception:
        # If embedding fails, don't break the app
        pass

# Apply the background/glass style
_set_background_glass("ugb1.png")

# Global modern theme: fonts, colors, animations, components polish
st.markdown('<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">', unsafe_allow_html=True)
st.markdown("""<style>
:root {
  --bg: #ffffff;
  --card: #ffffff;
  --muted: #1f2937; /* slate-800 for strong contrast on light bg */
  --text: #0f172a;  /* slate-900 as primary text */
  --brand: #16a34a;
  --brand-2: #0e7490;
  --brand-3: #6d28d9;
  --ring: rgba(15,23,42,0.25);
}
html, body, .stApp { font-family: Inter, system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, Noto Sans, Helvetica Neue, Arial, "Apple Color Emoji", "Segoe UI Emoji"; color: var(--text); }
.stApp::before, .stApp::after {
  content: "";
  position: fixed;
  inset: auto auto 10% -10%;
  width: 40vw;
  height: 40vw;
  background: radial-gradient(closest-side, rgba(34,197,94,0.18), transparent 65%);
  filter: blur(40px);
  z-index: 0;
  pointer-events: none;
}
.stApp::after {
  inset: -15% -10% auto auto;
  width: 35vw;
  height: 35vw;
  background: radial-gradient(closest-side, rgba(6,182,212,0.16), transparent 65%);
}
.stApp .main .block-container { position: relative; z-index: 1; }
.hero {
  background: linear-gradient(145deg, rgba(15,23,42,0.9), rgba(15,23,42,0.55));
  border: 1px solid rgba(255,255,255,0.06);
  border-radius: 20px;
  padding: 2.25rem;
  margin: 0.75rem 0 1.5rem 0;
  box-shadow: 0 12px 30px rgba(2,6,23,0.45);
}
.hero-title {
  font-family: Poppins, Inter, system-ui;
  font-weight: 800;
  letter-spacing: -0.02em;
  font-size: clamp(1.8rem, 2.5vw + 1.2rem, 3.25rem);
  margin: 0 0 .35rem 0;
  background: linear-gradient(90deg, #0f172a, #1f2937 45%, #0b1220 85%);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}
.hero-sub {
  color: var(--muted);
  font-size: 1.05rem;
  line-height: 1.6;
}
.hero-badges { display: flex; gap: .5rem; flex-wrap: wrap; margin-top: .85rem; }
.badge {
  font-size: .8rem;
  color: #0f172a;
  background: rgba(15,23,42,0.08);
  padding: .35rem .6rem;
  border-radius: 999px;
  border: 1px solid rgba(15,23,42,0.15);
  font-weight: 600;
}
.card {
  background: #ffffff;
  border: 1px solid rgba(2,6,23,0.08);
  border-radius: 16px;
  padding: 1.25rem;
  box-shadow: 0 10px 24px rgba(2,6,23,0.06);
  color: var(--text);
}
.card h4 { color: var(--text); margin: 0 0 .5rem 0; font-weight: 700; }
.card .hint { color: var(--muted); font-size: .92rem; margin-bottom: .75rem; }
.stButton > button {
  background: linear-gradient(135deg, var(--brand), #16a34a);
  color: white;
  border: 0;
  padding: .7rem 1rem;
  border-radius: 10px;
  width: 100%;
  font-weight: 600;
  box-shadow: 0 6px 14px rgba(16,185,129,0.28);
  transition: transform .08s ease, filter .2s ease, box-shadow .2s ease;
}
.stButton > button:hover { filter: brightness(1.05); box-shadow: 0 10px 18px rgba(16,185,129,0.32); }
.stButton > button:active { transform: translateY(1px); }
[data-testid="stFileUploader"] div[data-testid="stFileUploaderDropzone"] {
  border: 1px dashed rgba(2,6,23,0.15);
  background: #f8fafc;
  transition: border-color .2s ease, background .2s ease, box-shadow .2s ease;
  border-radius: 14px;
}
[data-testid="stFileUploader"] div[data-testid="stFileUploaderDropzone"]:hover {
  border-color: rgba(15,23,42,0.45);
  box-shadow: 0 8px 20px rgba(2,6,23,0.08);
  background: #f1f5f9;
}
[data-testid="stFileUploader"] section > div { color: #0f172a !important; }
[data-testid="stFileUploader"] label { color: #0f172a !important; font-weight: 600; }
[data-testid="stCameraInputLabel"] { color: #0f172a !important; font-weight: 600; }
@keyframes fadeUp { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }
.fade { animation: fadeUp .4s ease both; }
.input-section {
  background: rgba(2,6,23,0.75);
  border-radius: 14px;
  padding: 1rem;
  margin: 0.5rem 0;
  border: 1px solid rgba(255,255,255,0.06);
}
.section-title {
  color: #0f172a;
  font-size: 1.05rem;
  margin-bottom: 0.75rem;
  font-weight: 600;
}
</style>""", unsafe_allow_html=True)
try:
    _logo = Image.open("ugb1.png")
    _w, _h = _logo.size
    # Prevent zero or negative sizes
    _new_w = max(1, _w // 2)  # Changed from 4 to 2 to make image twice as large
    _new_h = max(1, _h // 2)
    _logo_small = _logo.resize((_new_w, _new_h), Image.LANCZOS)

    # Hero header with logo and gradient title
    with st.container():
        logo_col, text_col = st.columns([1, 3])
        with logo_col:
            st.image(_logo_small, use_column_width=False)
        with text_col:
            st.markdown("<div class='hero-title'>Birds in Uganda</div>", unsafe_allow_html=True)
            st.markdown(
                "<div class='hero-sub'>Identify birds from photos in seconds. Upload an image or use your camera to discover species, with a beautiful, distraction-free interface.</div>",
                unsafe_allow_html=True,
            )
            st.markdown(
                "<div class='hero-badges'><span class='badge'>Smart Vision</span><span class='badge'>On-device Capture</span><span class='badge'>UG Species Focus</span></div>",
                unsafe_allow_html=True,
            )
        st.markdown("</div>", unsafe_allow_html=True)
except Exception:
    # If logo not found or cannot be opened, skip silently
    pass

# Remove old italic banner to reduce clutter and rely on hero subtitle

# Main content container with modern layout
with st.container():
    # Section prompt
    st.markdown(
        """
        <div style='text-align:center; margin: .5rem 0 1rem;'>
            <p style='color:#0f172a; margin:0; font-weight:700; font-size:1rem; letter-spacing:.01em;'>
                Choose how you want to identify a bird
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    tab_upload, tab_camera = st.tabs(["📁 Upload", "📷 Camera"])

    with tab_upload:
        st.markdown("<h4>📁 Upload Image</h4>", unsafe_allow_html=True)
        st.markdown("<div class='hint'>PNG or JPEG. Clear, close-up shots improve results.</div>", unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Select a bird image", type=['png', 'jpg', 'jpeg'], key="uploader_file")
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image', use_column_width=True)
            st.button("Identify Specie", key="identify_specie_upload_button")
        st.markdown("</div>", unsafe_allow_html=True)

    with tab_camera:
        if 'camera_active' not in st.session_state:
            st.session_state.camera_active = False

        st.markdown("<h4>📷 Take Picture</h4>", unsafe_allow_html=True)
        if not st.session_state.camera_active:
            try:
                _placeholder_path = "ub2.png"
                if os.path.exists(_placeholder_path):
                    with open(_placeholder_path, "rb") as _f:
                        _data = _f.read()
                    _b64 = base64.b64encode(_data).decode()
                    _img_html = (
                        f"<img src=\"data:image/png;base64,{_b64}\" "
                        "style=\"width:100%; aspect-ratio:4/3; min-height:280px; object-fit:cover; "
                        "border-radius:12px; margin-bottom:0.75rem; box-shadow: inset 0 0 40px rgba(0,0,0,0.6);\"/>")
                    st.markdown(_img_html, unsafe_allow_html=True)
                else:
                    st.markdown(
                        "<div style='width:100%; aspect-ratio:4/3; min-height:280px; background:linear-gradient(180deg,#0b1220,#0b1220 60%, #0f172a); border-radius:12px; margin-bottom:0.75rem; box-shadow: inset 0 0 40px rgba(0,0,0,0.6);'></div>",
                        unsafe_allow_html=True,
                    )
            except Exception:
                st.markdown(
                    "<div style='width:100%; aspect-ratio:4/3; min-height:280px; background:linear-gradient(180deg,#0b1220,#0b1220 60%, #0f172a); border-radius:12px; margin-bottom:0.75rem; box-shadow: inset 0 0 40px rgba(0,0,0,0.6);'></div>",
                    unsafe_allow_html=True,
                )

            def _start_camera():
                st.session_state.camera_active = True

            st.button("Start Camera 📷", key="use_camera_button", on_click=_start_camera)

        if st.session_state.camera_active:
            camera_photo = st.camera_input("Take a photo", key="camera_input")
            if camera_photo is not None:
                image = Image.open(camera_photo)
                st.image(image, caption='Captured Photo', use_column_width=True)
                st.button("Identify Specie", key="identify_specie_camera_button")

            if st.button("Stop Camera ⏹️", key="stop_camera_button", help="Click to stop camera preview"):
                st.session_state.camera_active = False
        st.markdown("</div>", unsafe_allow_html=True)

    # Sidebar info
    with st.sidebar:
        st.markdown("""
        <div class='card fade'>
          <h4>About</h4>
          <div class='hint'>This demo helps identify birds commonly found across Uganda. For best results, ensure good lighting and a clear subject.</div>
        </div>
        """, unsafe_allow_html=True)

    # Footer
    st.markdown(
        """
        <div style='text-align:center; color:#334155; margin-top: 1rem; font-size:.9rem;'>
            Built for the Love of Nature
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    # (no wrapper divs to close)
