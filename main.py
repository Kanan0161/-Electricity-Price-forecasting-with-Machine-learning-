# Plot the correlation matrix
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", square=True)
plt.title("Correlation Matrix of Electricity Pricing and Weather Data")
plt.tight_layout()
plt.show()


#Plot Electricity Prices
ax = df.plot(x='datetime', y='Price', figsize=(15, 11))
ax.set_xlabel("Date")
ax.set_ylabel("Price (€/MWh)")
ax.set_title('Electricity Prices in Castlebar Co.mayo' )

plt.show()
