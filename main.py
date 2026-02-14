# Task 3: Task Automation - Move JPG Files (Simulation Version)

# Simulated list of files in a folder
files = ["image1.jpg", "doc1.txt", "photo.jpg", "notes.pdf", "pic.jpg"]

jpg_files = []

print("Scanning files...\n")

# Identify JPG files
for file in files:
    if file.endswith(".jpg"):
        jpg_files.append(file)

# Display moved files
print("JPG files moved:")
for file in jpg_files:
    print("Moved:", file)

print("\nAll JPG files moved successfully!")