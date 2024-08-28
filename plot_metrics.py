import matplotlib.pyplot as plt

# Initialize lists to store data
epochs = []
precisions = []
recalls = []

# Parse the results.txt file
with open('results.txt', 'r') as file:
    for line in file:
        if line.strip():  # Ignore empty lines
            parts = line.split()
            epoch = int(parts[0].split('/')[0])  # Extract the epoch number
            precision = float(parts[8])  # Assuming precision is at index 7
            recall = float(parts[9])     # Assuming recall is at index 8
            print(f"{epoch}: p: {precision}, r:{recall}")
            epochs.append(epoch)
            precisions.append(precision)
            recalls.append(recall)

# Plot precision and recall
plt.figure(figsize=(25, 10))
plt.plot(epochs, precisions, label='Precision', marker='o')
plt.plot(epochs, recalls, label='Recall', marker='o')

plt.xlabel('Epoch')
plt.ylabel('Metric Value')
plt.title('Precision and Recall vs. Epoch')
plt.legend()
plt.grid(True)
plt.savefig('precision_recall_vs_epochs.png')
plt.show()
