Name:		trader
Version:	7.4
Release:	%mkrel 1
Summary:	A simple game of interstellar trading
License:	GPLv3+
Group:		Games/Strategy
Url:		http://www.zap.org.au/software/trader/
Source0:	http://www.zap.org.au/software/trader/unix/%{name}-%{version}.tar.gz

BuildRequires:	gettext
BuildRequires:	gperf
BuildRequires:	ncurses-devel

%description
Star Traders is a simple game of interstellar trading, where the objective
is to create companies, buy and sell shares, borrow and repay money, in
order to become the wealthiest player (the winner).


%prep
%setup -q

%build
%configure
%make

%install
%makeinstall
%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%doc NEWS README
%doc %{_mandir}/man6/%{name}.6*
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6*
