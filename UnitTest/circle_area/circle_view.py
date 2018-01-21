import ui
import console
from circle import area


@ui.in_background
def btn_area_onclick(sender):
  view = sender.superview
  tarea = view['txt_area']
  tradius = view['txt_radius']
  try:
    tarea.text = '{:f}'.format(area(float(tradius.text)))
  except Exception as err:
    console.alert('Error', str(err))


v = ui.load_view()
v.present('sheet')

