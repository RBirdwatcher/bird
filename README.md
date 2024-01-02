
# What are BIRD watchers? :telescope:

BIRD watchers are documented test cases that can be programmatically extracted to "watch" a BIRD implementation and make sure it is correct.
These test cases can be considered unit-tests. We break these up into 2 categories:
* **Derivations**: Generation of Enriched Input Layer (EIL) attributes from Input Layer (IL) attributes
* **Report Mappings**: Generation of report cell values from EIL attributes

# Structure
Each watcher has 4 components:
  1. **Documentation**: A free-form collection of information that describes what the implementation should do from a business user's perspective. These are typically referred in the industry as business requirements. These should be clear, concise and thorough.
  2. **Tests**: A structured file(s) that conforms to the specified (JSON/CSV) test schema. The tests represent simple input/output examples that can be programmatically read and used to test software implementations.
  3. **Metadata**: A structured file that conforms to the specified (JSON/CSV) metadata schema. The metadata file should give a high-level overview of the watcher, what it is for, what it does and a direct link to where documentation/more information can be found.
  4. **Implementations**: These are actual executable files (SQL, Python etc.) contributed by community members and that pass all the tests. If a new test is added and an implementation no longer passes all the tests, it will need to be refactored in order to be included in the next release version.


# Running the tests in Github CodeSpaces

Open  the repository in a codespace by clicking on Code->CodeSpaces-> + in the github page (e.g. https://github.com/RBirdwatcher/bird/tree/main )
In the 'terminal' on the bottom right just type ./run_tests.sh and press return..you should see pass/fail output like:

@RBirdwatcher ➜ /workspaces/bird (main) $ ./run_tests.sh 

testing primary example

{'fwd_start': 'FALSE', 'start_date': '29/09/21', 'report_date': '01/10/21', 'end_date': '-', 'trade_date': '-', 'description': 'primary example'}

Passed

testing primary example

{'fwd_start': 'FALSE', 'start_date': '01/10/21', 'report_date': '01/10/21', 'end_date': '-', 'trade_date': '-', 'description': 'primary example'}

Passed

testing primary example

{'fwd_start': 'TRUE', 'start_date': '04/10/21', 'report_date': '01/10/21', 'end_date': '-', 'trade_date': '-', 'description': 'primary example'}

Failed

testing no start date (like equities held?)

{'fwd_start': 'FALSE', 'start_date': '-', 'report_date': '01/10/21', 'end_date': '-', 'trade_date': '-', 'description': 'no start date (like equities held?)'}

Passed

testing product ends on same day as it starts

{'fwd_start': 'TRUE', 'start_date': '29/09/21', 'report_date': '01/10/21', 'end_date': '29/09/21', 'trade_date': '-', 'description': 'product ends on same day as it starts'}

Failed

testing products traded before the reporting date but starting after for technical reasons

{'fwd_start': 'FALSE', 'start_date': '03/10/21', 'report_date': '01/10/21', 'end_date': '-', 'trade_date': '01/10/21', 'description': 'products traded before the reporting date but starting after for technical reasons'}

Passed

testing start date is weekend

{'fwd_start': 'FALSE', 'start_date': '02/10/21', 'report_date': '01/10/21', 'end_date': '-', 'trade_date': '01/10/21', 'description': 'start date is weekend'}

Passed





