# from datasets import Dataset, DatasetDict

# # Define file path
# file_path = "../data/openwebtext/data.txt"

# # Read file and preprocess to remove blank lines
# with open(file_path, "r") as file:
#     lines = [line.strip() for line in file if line.strip()]

# # Create a Hugging Face Dataset
# dataset = Dataset.from_dict({"text": lines})

# # Split the dataset into 80% train and 20% test
# train_test_split = dataset.train_test_split(test_size=0.2, seed=42)

# # Create a DatasetDict
# owt = DatasetDict({
#     "train": train_test_split["train"],
#     "test": train_test_split["test"]
# })

# # Save the DatasetDict
# save_path = "../data/owt"
# owt.save_to_disk(save_path)

from datasets import DatasetDict, concatenate_datasets

# Load the dataset (adjust the path to your dataset folder)
dataset_path = "../data/emotionload"
dataset = DatasetDict.load_from_disk(dataset_path)

# Combine the validation and test splits
combined_dataset = concatenate_datasets([dataset["validation"], dataset["test"]])

# Merge the train split with the combined validation and test
full_dataset = concatenate_datasets([dataset["train"], combined_dataset])

# Resplit into 80% train and 20% test
new_split = full_dataset.train_test_split(test_size=0.2, seed=42)

# Save the new dataset with 2 splits
new_dataset_path = "../data/emotion_load"
new_split.save_to_disk(new_dataset_path)