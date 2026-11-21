"""
Courier Tracking System

A console-based application to book parcels, update their delivery status,
track parcels, and search parcels by receiver name.
"""

STATUS_FLOW = ["Booked", "Picked Up", "In Transit", "Out for Delivery", "Delivered"]

# Each parcel is stored using its tracking ID as the dictionary key.
# The history list stores every status reached by that parcel.
parcels = {}
next_tracking_number = 1001


def generate_tracking_id():
    """Generate a unique tracking ID automatically."""
    global next_tracking_number

    tracking_id = f"CT{next_tracking_number}"
    next_tracking_number += 1
    return tracking_id


def book_parcel():
    """Collect parcel details and save a new parcel."""
    print("\n--- Book a Parcel ---")
    sender = input("Sender name: ").strip()
    receiver = input("Receiver name: ").strip()
    destination = input("Destination: ").strip()

    if not sender or not receiver or not destination:
        print("All fields are required. Parcel was not booked.")
        return

    tracking_id = generate_tracking_id()

    parcels[tracking_id] = {
        "sender": sender,
        "receiver": receiver,
        "destination": destination,
        "status": "Booked",
        "history": ["Booked"]
    }

    print(
        f"Parcel booked. Tracking ID: {tracking_id} | "
        f"Status: {parcels[tracking_id]['status']}"
    )


def update_status():
    """Move a parcel only to the next status in the delivery sequence."""
    print("\n--- Update Parcel Status ---")
    tracking_id = input("Enter tracking ID: ").strip().upper()

    if tracking_id not in parcels:
        print(f"Tracking ID {tracking_id} not found.")
        return

    parcel = parcels[tracking_id]
    current_status = parcel["status"]

    if current_status == "Delivered":
        print(
            f"Parcel {tracking_id} is already delivered. "
            "No further updates allowed."
        )
        return

    current_index = STATUS_FLOW.index(current_status)
    new_status = STATUS_FLOW[current_index + 1]

    parcel["status"] = new_status
    parcel["history"].append(new_status)

    print(f"Status updated: {current_status} -> {new_status}")


def track_parcel():
    """Display parcel details, status history, and current status."""
    print("\n--- Track a Parcel ---")
    tracking_id = input("Enter tracking ID: ").strip().upper()

    if tracking_id not in parcels:
        print(f"Tracking ID {tracking_id} not found.")
        return

    parcel = parcels[tracking_id]
    history = " -> ".join(parcel["history"])

    print(f"Tracking ID: {tracking_id}")
    print(f"Receiver: {parcel['receiver']}")
    print(f"Destination: {parcel['destination']}")
    print(f"History: {history}")
    print(f"Current status: {parcel['status']}")


def search_by_receiver():
    """Find and display all parcels matching a receiver's name."""
    print("\n--- Search by Receiver ---")
    receiver_name = input("Enter receiver name: ").strip().casefold()

    if not receiver_name:
        print("Please enter a receiver name.")
        return

    matches = []
    for tracking_id, parcel in parcels.items():
        if receiver_name in parcel["receiver"].casefold():
            matches.append((tracking_id, parcel))

    if not matches:
        print(f"No parcels found for receiver: {receiver_name}")
        return

    print(f"\nParcels found: {len(matches)}")
    for tracking_id, parcel in matches:
        print(
            f"Tracking ID: {tracking_id} | "
            f"Receiver: {parcel['receiver']} | "
            f"Destination: {parcel['destination']} | "
            f"Status: {parcel['status']}"
        )


def display_menu():
    """Display the main menu."""
    print("\n========== COURIER TRACKING SYSTEM ==========")
    print("1. Book parcel")
    print("2. Update status")
    print("3. Track parcel")
    print("4. Search by receiver")
    print("5. Exit")


def main():
    """Run the application until the user selects Exit."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            book_parcel()
        elif choice == "2":
            update_status()
        elif choice == "3":
            track_parcel()
        elif choice == "4":
            search_by_receiver()
        elif choice == "5":
            print("Thank you for using the Courier Tracking System.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
