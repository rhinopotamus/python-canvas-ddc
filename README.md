# python-canvas-ddc
Automating the due date change process with Google Forms and Canvas.

Here is the workflow that this script will hopefully automate:
- A student submits a due date change request to my Google Form.
- This request gets shoved into a Google Sheet.
- Script scrapes the relevant information from the Google Sheet.
- Script plugs into the Canvas API and figures out what assignment the student is talking about.
    - I'm going to use the canvasapi package to abstract this for me.
- Script displays to me a summary of the changes it wants to make to Canvas due dates, and asks me to push a big red button to do them.
- Script plugs into the Canvas API to commit those changes to Canvas.

Other features on the wishlist:
- The script displays a summary of due date changes it's made for each student. 
- The script keeps state (probably on the Google Sheet) of which requests it's already processed.
- Would actually be rad to avoid the google form altogether. What if I hosted an interface to this script on my githubio? They could enter their email address, I could figure out what classes they have and build a list of due-date-changeable assignments for them to pick.
- Automatically send a confirmation email to the student.

Things I need to know to do this:
- which student 
    - I'm going to look them up by email, and Google Forms validates that input.
- which course
    - Google Forms has radio buttons for this; I'm looking up the pre-defined string in a dictionary of the courses for the term. (Will need to update that dictionary on a term-by-term basis.)
- which assignment
    - Students type something in. I'm going to use fuzzy string matching to guess which assignment they mean. This probably works ok given the limited range of inputs. Helper function `find_assignment` builds a dropdown widget.
- which new due date they want
    - Google Forms date picker. Comes out as mm/dd, so I can use datetime's stringer functions to read it in correctly.

1/31: So at this point I have all the helper functions I need. Todo:
- Build the frontend that allows me to confirm the request before it gets pushed through the API.
    - For each request:
        - Display student name
        - Show assignment picker dropdown so I can compare to their submitted string
        - Display requested new due date
        - Click a button to fire the request to the API. (Should I worry about batching?)
- Write "Done" to the status column in the spreadsheet.
- Send a confirmation email to the student?