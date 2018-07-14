# file-rename-datetime

## Rename files to begin with YYYY-MMDD with sequential iteration (0001-0002)

Append current YYYY-MMDD date format in sequence and rename all files in the **current directory**.
1. Current datetime will be used;
2. Iterates through a sequence beginning from 0001;
3. Maintains and appends to the original filename; and
4. Existing files starting with YYYY-MMDD will be skipped.

### Example Output:
- _workflow.docx_     --> 2018-0707 0001 workflow.docx
- _schedules.docx_    --> 2018-0707 0002 schedules.docx
- _letter_offer.docx_ --> 2018-0707 0003 letter_offer.docx

### To-Do-List

- [ ] Look up EXIF data and retrieve relevant values
- [ ] Include option to get creation time via os.path.getctime()
