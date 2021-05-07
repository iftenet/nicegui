from nice_gui import ui
from datetime import datetime

ui.label('Hello, Nice GUI!')

with ui.row() as row:
    row.button('BUTTON', on_click=lambda: row.label('Nice!'))
    with row.column() as column:
        column.button('BUTTON2')
        column.label("LABEL")

time = ui.label('Time:')
def update_time():
    time.text = f'Time: {datetime.now().strftime("%H:%M:%S")}'
ui.timer(1.0, update_time)