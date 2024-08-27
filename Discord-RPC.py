# Assuming you have not changed the general structure of the template no modification is needed in this file.
from . import commands
from .lib import fusionAddInUtils as futil
import adsk.core, adsk.fusion, adsk.cam, traceback
from .modules import pypresence 
import time

client_id = '1278012634247200880'
RPC = pypresence.Presence(client_id) 
RPC.connect()

app = adsk.core.Application.get()
ui = app.userInterface

def run(context):
    try:
        # This will run the start function in each of your commands as defined in commands/__init__.py
        commands.start()
    except:
        futil.handle_error('run')

def read():
    while True:
        update_rpc()
        time.sleep(500)

def stop(context):
    try:
        # Remove all of the event handlers your app has created
        futil.clear_handlers()

        # This will run the start function in each of your commands as defined in commands/__init__.py
        commands.stop()
        RPC.close()

    except:
        futil.handle_error('stop')

def get_project_name():
    try: 
        dataFile = app.activeDocument.dataFile
        project = dataFile.parentProject
        return project.name if project else "Not in a project"
    except: 
        return "Unknown project"
    
def get_item_name():
    try:
        document = app.activeDocument
        return document.name if document else "Not in a document"
    except:
        return "Unknown Item"


def update_rpc():
    RPC.update(
        state=f"Working on: {get_item_name()}",  # This will appear as the second line
        details=f"Project: {get_project_name()}",  # This will appear as the first line
        large_image="fusion360-logo",  # The key of the large image you uploaded
        large_text="Autodesk Fusion360",  # Text displayed when hovering over the large image
    )
