import matplotlib.pyplot as plt
import os

# --- Function to Count k-mers ---
def count_kmers(sequence, k):
    """Counts occurrences of each k-mer in the genome sequence."""
    kmer_counts = {}
    for i in range(len(sequence) - k + 1):
        kmer = sequence[i:i + k]
        kmer_counts[kmer] = kmer_counts.get(kmer, 0) + 1
    return kmer_counts

# ---  ORI Detection (Best Position) ---
def find_ori_candidate(sequence, k, window_size, min_frequency):
    """Finds the most likely ORI candidate based on highest k-mer frequency."""
    kmer_counts = {}
    ori_position = None  # Store the most likely ORI position
    max_kmer_frequency = 0  # Store the highest frequency found

    # Scan across genome using a sliding window
    for i in range(len(sequence) - window_size):
        window_seq = sequence[i:i + window_size]
        local_kmer_counts = count_kmers(window_seq, k)  # Count k-mers in the current window

        # Find the most frequent k-mer in this window
        most_frequent_kmer = max(local_kmer_counts, key=local_kmer_counts.get, default=None)
        if most_frequent_kmer and local_kmer_counts[most_frequent_kmer] > max_kmer_frequency:
            max_kmer_frequency = local_kmer_counts[most_frequent_kmer]
            ori_position = i  # Update with the best ORI candidate

    return ori_position
# --- Function to Open Images ---
def open_image(image_path):
    """Opens an image file automatically after saving."""
    if os.name == "nt":  # Windows
        os.startfile(image_path)
    elif os.name == "posix":  # macOS & Linux
        os.system(f"open {image_path}" if "darwin" in os.sys.platform else f"xdg-open {image_path}")

# --- Optimized k-mer Frequency Distribution Plot ---
def plot_kmer_distribution(kmer_counts, output_path="kmer_distribution.png"):
    """Plots the top 20 most frequent k-mers."""
    top_kmers = dict(sorted(kmer_counts.items(), key=lambda x: x[1], reverse=True)[:20])
    kmer_names = list(top_kmers.keys())
    kmer_frequencies = list(top_kmers.values())

    plt.figure(figsize=(10, 5))
    plt.bar(kmer_names, kmer_frequencies, color='skyblue', align='center')
    plt.xlabel("K-mers")
    plt.ylabel("Frequency")
    plt.title("Top 20 Most Frequent k-mers")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    print(f" K-mer distribution saved as {output_path}")
    open_image(output_path)

# --- Function to Plot ORI Candidate ---
def plot_ori_candidate(ori_position, genome_length, output_path="ori_candidate.png"):
    """Plots the most likely ORI candidate position on the genome."""
    plt.figure(figsize=(10, 3))
    plt.scatter([ori_position], [1], color='red', label="Best ORI Candidate", s=100)
    plt.xlim(0, genome_length)
    plt.xlabel("Genome Position (bp)")
    plt.ylabel("Detection Marker")
    plt.title("Detected ORI Region in E. coli")
    plt.legend()
    plt.tight_layout()
    
    plt.savefig(output_path)  
    plt.show()  

# -- Load Genome Data --
genome_path = "C:\\Users\\zackd\\Downloads\\E_coli.txt"  # Update with correct path
with open(genome_path, 'r') as file:
    genome_sequence = file.read().strip()

# -- Set Parameters --
kmer_length = 12
window_size = 1000
min_occurrences = 5

# --- Process Data ---
kmer_counts = count_kmers(genome_sequence, kmer_length)
ori_position = find_ori_candidate(genome_sequence, kmer_length, window_size, min_occurrences)

# --- Plot Graphs ---
plot_kmer_distribution(kmer_counts)
plot_ori_candidate(ori_position, len(genome_sequence))

# --- Print Results ---
print(f"Best ORI candidate position: {ori_position}")  