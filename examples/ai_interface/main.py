#!/usr/bin/env python3
import asyncio
import functools
import io
from typing import Callable

import replicate  # very nice API to run AI models; see https://replicate.com/
from nicegui import ui
from nicegui.events import UploadEventArguments


async def io_bound(callback: Callable, *args: any, **kwargs: any):
    '''Makes a blocking function awaitable; pass function as first parameter and its arguments as the rest'''
    return await asyncio.get_event_loop().run_in_executor(None, functools.partial(callback, *args, **kwargs))


async def transcribe(args: UploadEventArguments):
    transcription.text = 'Transcribing...'
    model = replicate.models.get('openai/whisper')
    prediction = await io_bound(model.predict, audio=io.BytesIO(args.files[0]))
    text = prediction.get('transcription', 'no transcription')
    transcription.set_text(f'result: "{text}"')


async def generate_image():
    image.source = 'https://dummyimage.com/600x400/ccc/000000.png&text=building+image...'
    model = replicate.models.get('stability-ai/stable-diffusion')
    prediction = await io_bound(model.predict, prompt=prompt.value)
    image.source = prediction[0]

# User Interface
with ui.row().style('gap:10em'):
    with ui.column():
        ui.label('OpenAI Whisper (voice transcription)').classes('text-2xl')
        ui.upload(on_upload=transcribe).style('width: 20em')
        transcription = ui.label().classes('text-xl')
    with ui.column():
        ui.label('Stable Diffusion (image generator)').classes('text-2xl')
        prompt = ui.input('prompt').style('width: 20em')
        ui.button('Generate', on_click=generate_image).style('width: 15em')
        image = ui.image().style('width: 60em')

ui.run()
