Summary:	Load-and-go assembler for Donald Knuth's MIX language
Summary(pl):	Asembler dla jêzyka MIX Donalda Knutha
Name:		mixal
Version:	1.08
Release:	3
License:	distributable
Group:		Development/Languages
Source0:	http://locke.ccil.org:/pub/esr/%{name}_%{version}.orig.tar.gz
# Source0-md5:	46b7fa9a94b3f9f82a81399e6f2b47b3
Patch0:		%{name}_1.08-7.diff.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mixal is an assembler and interpreter for Donald Knuth's mythical MIX
computer, defined in: Donald Knuth, "The Art of Computer Programming",
Vol. 1: Fundamental Algorithms_. Addison-Wesley, 1973 (2nd ed.)

%description -l pl
Mixal to asembler i interpreter dla mitycznego komputera MIX Donalda
Knutha, zdefiniowanego w pierwszej czê¶ci "Fundamental Algorithms"
ksi±¿ki Donalda Knutha "The Art of Computer Programming", wydanej
przez Addison-Wesley w 1973 roku (drugie wydanie).

%prep
%setup -q -n %{name}-%{version}.orig
%patch -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d ${RPM_BUILD_ROOT}%{_bindir}
install -d ${RPM_BUILD_ROOT}%{_mandir}/man1

install mixal ${RPM_BUILD_ROOT}%{_bindir}/mixal
install mixal.1 ${RPM_BUILD_ROOT}%{_mandir}/man1/mixal.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc READ.ME NOTES
%attr(755,root,root) %{_bindir}/mixal
%{_mandir}/man1/*.1*
