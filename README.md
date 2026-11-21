# Courier Tracking System (PS No. 80)

## Project overview
A Python 3 console application for a courier office. It can book parcels, update
delivery status, track parcel history, and search parcels by receiver name.

## Features
- Automatically generates unique tracking IDs (CT1001, CT1002, ...).
- Stores parcel details in a dictionary.
- Stores each parcel's status history in a list.
- Allows only forward status movement:
  Booked -> Picked Up -> In Transit -> Out for Delivery -> Delivered
- Prevents updates after a parcel is Delivered.
- Searches receiver names without case sensitivity.
- Handles unknown tracking IDs and invalid menu choices.

## Requirements
- Python 3
- No external libraries are required.

## How to run
1. Download `courier_tracking_system.py`.
2. Open a terminal in the folder containing the file.
3. Run:

   `python courier_tracking_system.py`

   On some systems, use `python3 courier_tracking_system.py`.

## Menu
1. Book parcel
2. Update status
3. Track parcel
4. Search by receiver
5. Exit

## Test case walkthrough
The program starts with an empty in-memory system. Follow the steps in order:

### Test Case 1 — Normal input
1. Choose `1`.
2. Sender: `Neha`
3. Receiver: `Karan`
4. Destination: `Nagpur`

Expected: `Parcel booked. Tracking ID: CT1001 | Status: Booked`

### Test Case 2 — Boundary / minimum input
1. Choose `2`.
2. Tracking ID: `CT1001`

Expected: `Status updated: Booked -> Picked Up`

### Test Case 3(a) — Invalid tracking ID
1. Choose `3`.
2. Tracking ID: `CT9999`

Expected: `Tracking ID CT9999 not found.`

### Test Case 3(b) — Parcel already Delivered
To create the parcel referred to in the question, choose `1` and enter any valid
details. It will receive ID `CT1002`. Then choose `2` four times for `CT1002` to
move it through Picked Up, In Transit, Out for Delivery, and Delivered.
Choose `2` once more for `CT1002`.

Expected: `Parcel CT1002 is already delivered. No further updates allowed.`

### Test Case 4 — Different valid scenario
1. Choose `2` and enter `CT1001`.

Expected: `Status updated: Picked Up -> In Transit`
2. Choose `3` and enter `CT1001`.

Expected details include:
- Tracking ID: CT1001
- Receiver: Karan
- Destination: Nagpur
- History: Booked -> Picked Up -> In Transit
- Current status: In Transit

## Important note
Parcel records are stored in memory, so they are cleared when the program is
closed. This matches the assignment's dictionary-based requirement. Persistent
file/database storage was not requested.
