const $ = id => document.getElementById(id);

async function refresh() {
  const data = await fetch("/api/data").then(r => r.json());
  $("total").textContent = data.total.toFixed(2);
  $("accounts").innerHTML = data.accounts.map(a =>
    `<tr><td>${a.number}</td><td>${a.customer.name}</td><td>${a.type}</td><td>${a.customer.phone}</td><td>₹${a.balance.toFixed(2)}</td></tr>`
  ).join("");
  $("transactionsList").innerHTML = data.transactions.map(t =>
    `<tr><td>${t.account}</td><td>${t.action}</td><td>₹${t.amount.toFixed(2)}</td></tr>`
  ).join("");
}

$("createForm").onsubmit = async e => {
  e.preventDefault();
  const body = Object.fromEntries(new FormData(e.target));
  const r = await fetch("/api/create", {method:"POST", headers:{"Content-Type":"application/json"}, body:JSON.stringify(body)});
  const result = await r.json();
  $("createMessage").textContent = result.error || `Account created: ${result.number}`;
  if (r.ok) { e.target.reset(); refresh(); }
};

$("actionForm").onsubmit = async e => {
  e.preventDefault();
  const body = Object.fromEntries(new FormData(e.target));
  const r = await fetch("/api/action", {method:"POST", headers:{"Content-Type":"application/json"}, body:JSON.stringify(body)});
  const result = await r.json();
  alert(result.error || result.message);
  if (r.ok) { e.target.reset(); refresh(); }
};

refresh();
