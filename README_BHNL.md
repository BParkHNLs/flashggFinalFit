# BHNL-based instructions

### Installation
Follow the instructions in the [README.md](./README.md), keeping in mind the different repository.

### Run-time
Currently we only use the [f-test](./Background/test/fTest.cpp) routine in this tool.
The routine is steered by a [submitter](./Background/submitFtest.py), which runs the f-test in each analysis category and in each specified window. All is done sequentially.

```
cd Background
make
python submitFtest.py
```
