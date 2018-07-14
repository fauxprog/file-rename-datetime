# Python: Rename Files (adding date and numbering)

This script appends current YYYY-MMDD date format in sequence (0001-0002) and rename all files in the **current directory**.
1. Current datetime will be used;
2. Iterates through a sequence beginning from 0001;
3. Maintains and appends to the original filename; and
4. Existing files starting with YYYY-MMDD will be skipped.

## Example Output
- _workflow.docx_     --> 2018-0718 0001 workflow.docx
- _schedules.docx_    --> 2018-0718 0002 schedules.docx
- _letter_offer.docx_ --> 2018-0718 0003 letter_offer.docx

## Instructions
To change the order of the year-month-date, refer to `YMD` variable where:

`YMD = datetime.date.today().strftime("%Y-%m%d")`

`%Y` displays "YYYY", `%m` displays "mm", `%d` displays "dd"

- `(%d%m%Y)`: Output will display 18072018
- `(%Y-%m-%d)`: Adding symbols (such as dashes) will display 2018-07-18 

The order of the final output can be changed, refer to `new_fname` variable where:

`new_fname = (f"{YMD} {numseq} {ori_fname} {fext}")`
- Since the variables are contained within the f-string `(f" ... ")` the first 3 variables can be moved around. The last variable `{fext}` must always remain at the end.

For more information refer to [Python documentation on datetime](https://docs.python.org/3/library/datetime.html)



## To-Do-List:

- [ ] Look up EXIF data and retrieve relevant values
- [ ] Include option to get creation time via `os.path.getctime()`
