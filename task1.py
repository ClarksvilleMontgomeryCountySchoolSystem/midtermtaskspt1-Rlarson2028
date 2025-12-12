# Calculate milestone progress
current_milestone = current_followers // milestone_increment
progress_in_milestone = current_followers % milestone_increment

# Calculate growth statistics
total_gained = current_followers - starting_followers
daily_average = total_gained // days_tracked

# Calculate projections
days_to_milestone = (milestone_increment - progress_in_milestone) // daily_average
weekly_growth = daily_average * 7

# Display results with f-strings
print(f"Creator: {creator_name}")
print(f"Current Milestone: {current_milestone}")
print(f"Progress in Milestone: {progress_in_milestone} followers")
print(f"Total Growth: {total_gained} followers")
print(f"Daily Average: {daily_average} followers")
print(f"Days to Next Milestone: {days_to_milestone} days")
print(f"Weekly Growth Projection: {weekly_growth} followers")

