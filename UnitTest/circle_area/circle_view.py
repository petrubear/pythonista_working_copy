import ui
from circle import area

def btn_area_onclick(sender):
  view = sender.superview
  tarea = view['txt_area']
  tradius = view['txt_radius']
  tarea.text = '{:f}'.format(area(float(tradius.text)))
    
    
v = ui.load_view()
v.present('sheet')

