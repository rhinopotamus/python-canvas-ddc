# python-canvas-ddc
Automating the due date change process with Google Forms and Canvas.

Here is the workflow that this script will hopefully automate:
- A student submits a due date change request to my Google Form.
- This request gets shoved into a Google Sheet.
- Script scrapes the relevant information from the Google Sheet.
- Script plugs into the Canvas API and figures out what assignment the student is talking about.
- Script displays to me a summary of the changes it wants to make to Canvas due dates, and asks me to push a big red button to do them.
- Script plugs into the Canvas API to commit those changes to Canvas.

Other features on the wishlist:
- The script displays a summary of due date changes it's made for each student. 
- The script keeps state (probably on the Google Sheet) of which requests it's already processed.

The fun part is that I don't know how to do literally any of this.
