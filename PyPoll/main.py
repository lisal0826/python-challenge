import os

# Set the file paths
input_file_path = "Resources/election_data.csv"
output_file_path = "analysis/election_results.txt"

try:
    # Read the CSV file and store data in a list of dictionaries
    with open(input_file_path, "r") as file:
        # Skip the header
        next(file)
        data = [line.strip().split(",") for line in file]

    # Calculate the total number of votes cast
    total_votes = len(data)

    # Create a dictionary to store candidate vote counts
    candidate_votes = {}

    # Count votes for each candidate
    for entry in data:
        candidate = entry[2]  # Assuming "Candidate" is at index 2
        candidate_votes[candidate] = candidate_votes.get(candidate, 0) + 1

    # Calculate percentages
    candidate_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

    # Find the winner based on popular vote
    winner = max(candidate_votes, key=candidate_votes.get)

    # Print the results
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")

    for candidate, votes in candidate_votes.items():
        print(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({votes})")

    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    # Save the results to a text file in the specified output path
    output_dir = os.path.dirname(os.path.abspath(output_file_path))
    os.makedirs(output_dir, exist_ok=True)

    with open(output_file_path, "w") as f:
        f.write("Election Results\n")
        f.write("-------------------------\n")
        f.write(f"Total Votes: {total_votes}\n")
        f.write("-------------------------\n")

        for candidate, votes in candidate_votes.items():
            f.write(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({votes})\n")

        f.write("-------------------------\n")
        f.write(f"Winner: {winner}\n")
        f.write("-------------------------\n")

except Exception as e:
    print(f"An error occurred: {e}")
