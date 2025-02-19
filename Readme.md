# 🧬 Finding the Origin of Replication (ORI) in *E. coli*  

## 📌 Overview  
This project analyzes the **E. coli genome** to identify the **Origin of Replication (ORI)**—the region where DNA replication begins. Using **k-mer frequency analysis** and **clump detection**, I searched for **highly repetitive DNA sequences**, a key characteristic of ORI sites.  

---

## 🔬 Methodology  

### 1️⃣ **Preprocessing the Genome Data**  
- 📌 Used the full **E. coli** genome sequence.  
- 🧹 Cleaned and formatted the data for analysis.  

### 2️⃣ **Identifying Frequent k-mers**  
- 🧮 Applied a **sliding window approach** to count occurrences of k-length substrings.  
- 📊 Plotted **k-mer frequency distributions** to detect repetitive patterns.  

### 3️⃣ **Clump Finding Algorithm**  
- 🔎 Detected **k-mers appearing multiple times** within short genome regions.  
- 🧬 The most frequent **k-mers are strong ORI candidates**.  

---

## ⚡ Optimization: Using a Right Shift for Efficiency  

### **How It Works**  
Instead of **recomputing k-mer frequencies from scratch** for each new window, I used a **right shift** (sliding window) approach:  
1️⃣ **Initialize the first window** → Compute k-mer frequencies in the first **L-length** segment.  
2️⃣ **Slide the window right by one position** →  
   - ❌ **Remove** the **leftmost k-mer** from the frequency map.  
   - ✅ **Add** the **new rightmost k-mer** entering the window.  
3️⃣ **Check for frequent k-mers** in the updated window.  

### **Why This is More Efficient?**  
✅ Reduces time complexity from **O(nL) → O(n)**.  
✅ Avoids redundant recalculations, making it **suitable for large genomes**.  

---

## 📂 Dataset  
| File       | Source  | Description |
|------------|--------|-------------|
| `E_coli.txt` | [NCBI GenBank](https://www.ncbi.nlm.nih.gov/genbank/) | Full *E. coli* genome sequence |

---

## 📊 Key Findings  
- ✅ **Frequent k-mers (9-mers) formed clumps** in a specific genome region.  
- ✅ The top candidate regions **match known ORI markers**.  
- ✅ Further validation is needed with **genome annotation**.  

---

## 🚀 How to Run the Code  

### **Option 1: Run in Python**  
```bash
# Clone the repository
git clone https://github.com/yourusername/ecoli-ori-analysis.git
cd ecoli-ori-analysis

📈 Visualization Example
[![Kmer distribution](https://github.com/user-attachments/assets/b53abc74-c9c9-4069-ae15-78f20cbe01ca)](https://imgur.com/a/DdMUXiz)
![ori_candidate](https://github.com/user-attachments/assets/b5e4890a-fc44-4232-a807-f4d10acab7ea)(https://imgur.com/hNOMR4H)



🛠 Technologies Used
✅ Python (NumPy, Pandas)
✅ Algorithm Design (Sliding Window, Clump Finding)
✅ Matplotlib & Seaborn (for Visualization)


👨‍💻 Author
👤 Zackary Davis – Aspiring Data Scientist with a background in Biomedicine
