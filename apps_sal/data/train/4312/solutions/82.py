def pick_peaks(arr):
    return_dict = {"pos": [], "peaks": []}
    fall = False
    peak = False
    plateaus_after_peak = False
    plateaus = False
    plateaus_pos = 0

    for position, current in enumerate(arr):

        if position == 0:
            print(f"[{position}] {current} - START")
        elif position == len(arr) - 1:
            print(f"[{position}] {current} - END")

        else:

            next = arr[position + 1]
            previous = arr[position - 1]

            if previous > current < next:
                fall = True
                peak = False
                plateaus_after_peak = False
                plateaus = False
                print(f"[{position}] {current} - Fell!")

            elif previous > current > next:
                fall = True
                peak = False
                plateaus_after_peak = False
                plateaus = False
                print(f"[{position}] {current} - Falling...")

            elif previous < current < next:
                fall = False
                peak = False
                plateaus_after_peak = False
                plateaus = False
                print(f"[{position}] {current} - Rising...")

            elif previous < current == next:
                fall = False
                peak = True
                plateaus_after_peak = False
                plateaus = True
                plateaus_pos = position
                print(f"[{position}] {current} - Plateaus start!")

            elif previous == current > next:

                if position == 1:
                    print(f"[{position}] {current} - End of starting plateaus!")

                # jeśli nie drugi i nie przedostatni
                elif position != 1 and position != len(arr) - 2:

                    if plateaus_after_peak:
                        fall = True
                        peak = False
                        plateaus_after_peak = False
                        plateaus = False
                        print(f"[{position}] {current} - Plateus End after peak - Falling...")

                    else:
                        fall = True
                        peak = False
                        plateaus_after_peak = False
                        plateaus = False
                        print(f"[{position}] {current} - End of plateaus! Falling, saving the start of plateaus!")
                        return_dict["pos"].append(plateaus_pos)
                        return_dict["peaks"].append(current)
                elif position == len(arr) - 2 and current > next and not plateaus_after_peak:
                    fall = True
                    peak = False
                    plateaus_after_peak = False
                    plateaus = False
                    print(f"[{position}] {current} - End of plateaus! Falling, saving the start of plateaus!")
                    return_dict["pos"].append(plateaus_pos)
                    return_dict["peaks"].append(current)

            elif previous > current == next:
                fall = False
                peak = False
                plateaus_after_peak = True
                plateaus = True
                print(f"[{position}] {current} - Plateus start after a peak!")

            elif previous < current > next:
                fall = False
                peak = True
                plateaus_after_peak = False
                plateaus = False
                print(f"[{position}] {current} - Its a peak! Saving")
                return_dict["pos"].append(position)
                return_dict["peaks"].append(current)

            elif previous == current == next:
                fall = False
                plateaus = True
                print(f"[{position}] {current} - Plateus Flat!")
            elif previous == current < next:
                if plateaus_after_peak:
                    fall = True
                    peak = False
                    plateaus_after_peak = False
                    plateaus = False
                    print(f"[{position}] {current} - Plateus End after peak - Rising...")
            elif plateaus:
                if position + 1 == len(arr) - 1:  # jesli nie jest przedostatni
                    if not plateaus_after_peak:
                        fall = False
                        peak = True
                        plateaus_after_peak = False
                        plateaus = False
                        print(f"[{position}] {current} - Plateus Before End")
                        return_dict["pos"].append(plateaus_pos)
                        return_dict["peaks"].append(current)
                    else:
                        print(f"[{position}] {current} - X1!")
                else:
                    print(f"[{position}] {current} - X2!")

            else:
                print(f"[{position}] {current} - OUTSIDE!")

    return return_dict
