import gradio as gr

from utils import generate_audio


with gr.Blocks() as demo:
    gr.Markdown('<center><h1>Vietnamese TTS Demo</h1></center>')
    gr.Markdown('To use our application, now input your prompt to the box below and click to Run button to hear your audio')

demo = gr.Interface(
    fn=generate_audio,
    inputs=[
        gr.Textbox(label='Prompt'),
        gr.components.Dropdown(label='Voice preset',
                               choices=['v2/en_speaker_0', 'v2/hi_speaker_0'])
    ],
    outputs=gr.components.Audio(label='Generated audio'),
    allow_flagging='never'                                                                                                                                                    
)

# Launch the app
if __name__ == '__main__':
    demo.launch() 