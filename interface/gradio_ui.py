import gradio as gr


with gr.Blocks() as demo:
    gr.Markdown('<center><h1>Vietnamese TTS Demo</h1></center>')
    gr.Markdown('To use our application, now input your prompt to the box below and click to Run button to hear your audio')

    prompt = gr.Textbox(label='Prompt', 
                        placeholder='Your prompt include yout description and the style which you want to generate')

    with gr.Group():
        with gr.Row():
            generate_btn = gr.Button(variant='primary', 
                                     size='small')
            code_btn = gr.Button(variant='secondary',
                                 size='small')

# Launch the app
demo.launch()